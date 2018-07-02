
function loadData (method, url) {
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			render(JSON.parse(this.responseText));
		}
	}
	xhr.open(method, url, true);
	xhr.send('');
}

function getListUl (list) {
	var result = '';
	for (var i = 0; i < list.length; i++) result += '<li><a href="' + list[i][1] + '"' + list[i][0] + '</a></li>';
	return '<ul>' + result + '</ul>';
}

function render (data) {
	document.getElementsByClassName('starter-template')[0].innerHTML = getListUl(data.goals);
}

loadData('GET', '/goals/');