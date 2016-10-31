function hideLoader() {
	$(".loader").hide();
}

function addSymptom(symptom) {
	$("#symptoms").after("<li>" + symptom + "</li>");
}

function writeData(data) {
	if (data !== null) {
		document.getElementById("$ID").innerHTML = data;
	} else {
		document.getElementById("$ID").innerHTML = "<h1>NO RESULTS FOUND</h1>";
	}

}
function getData(term) {
	$(".loader").show(500);
	$.get("search.php", {"term" : term} , function(data) {
		writeData(data);
		$(".loader").hide(500);
	});
}

function cancer() {
	document.write('<body style="background-image: url(images/cancer.png)" ><a href=""><div style="width: 100%; height: 100%;"></div></a></body></a>');
}
