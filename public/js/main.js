var xhr = new XMLHttpRequest();
xhr.open('GET', '/goals/', true);
xhr.onreadystatechange = function() {
	if (xhr.readyState === 4)
		if (xhr.status === 200)
			alert(xhr.responseText);
	alert("error!");
}
xhr.send('')