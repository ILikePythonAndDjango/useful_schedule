function replaceUrl(url, func=render, post=false) {
	window.history.pushState({url: window.location.href}, '', window.location.href);
	window.history.replaceState({url: url}, '', url);
	loadData(post ? 'POST' : 'GET', url, func);

}

function loadData (method, url, func) {
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = function() {
		if (this.readyState == 4 && this.status == 200) {
			func(JSON.parse(this.responseText));
		}
	}
	xhr.open(method, url, true);
	xhr.send('');
}


/* functions which drawn HTML tags */
function getListUl (list) {
	//return ul list with goals
	var result = '';
	for (var i = 0; i < list.length; i++) result += '<li id="' + list[i][2] + '"><a href="#" onclick="replaceUrl(\'/goals/' + list[i][2] + '/\', renderGoal)">' + list[i][0] + '</a></li>';
	return '<ul>' + result + '</ul>';
}

function getViewGoal(goal){
	//return HTML view some goal
	return '<h2>' + goal.title + '</h2><p> deadline: ' 
	+ goal.deadline + '</p><hr><p>' + goal.content + '</p>';
}
/* functions which drawn HTML tags */

/* functions which render HTML tags */
function render (data) {

	//render own template with context
	document.getElementsByClassName('starter-template')[0].innerHTML = getListUl(data.goals);
}

function renderGoal(data) {
	document.getElementsByClassName('starter-template')[0].innerHTML = getViewGoal(data);
}
/* functions which render HTML tags */