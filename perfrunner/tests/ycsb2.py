from perfrunner.helpers.cbmonitor import with_stats
from perfrunner.helpers.worker import ycsb_data_load_task, ycsb_task
from perfrunner.tests import PerfTest
from perfrunner.tests.n1ql import N1QLTest


class YCSBTest(PerfTest):

    def download_ycsb(self):
        self.worker_manager.init_ycsb_repo()

    def load(self, *args, **kwargs):
        PerfTest.load(self, task=ycsb_data_load_task)

    @with_stats
    def access(self, *args, **kwargs):
        PerfTest.access(self, task=ycsb_task)

    def run(self):
        self.download_ycsb()

        self.load()
        self.wait_for_persistence()
        self.check_num_items()

        self.access()

        self.report_kpi()


class YCSBThroughputTest(YCSBTest):

    def _report_kpi(self):
        self.reporter.post(
            *self.metrics.ycsb_throughput()
        )


class YCSBN1QLTest(YCSBTest, N1QLTest):

    def run(self):
        self.download_ycsb()

        self.load()
        self.wait_for_persistence()
        self.check_num_items()

        self.build_index()

        self.access()

        self.report_kpi()


class YCSBN1QLThroughputTest(YCSBN1QLTest, YCSBThroughputTest):

    pass
