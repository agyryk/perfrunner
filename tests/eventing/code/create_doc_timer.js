function OnUpdate(doc, meta) {
	var expiry = Math.round((new Date()).getTime() / 1000) + 7200;
	docTimer(timerCallback, meta.id, expiry);
}
function timerCallback(docid) {
}
