var DIV = '#content';
var CREATE = '<button class="btn btn-outline-success my-2 my-sm-0" type="submit" onclick="">Create</button>';

function ajaxRequest(url, render=renderUlList, properties={}, dataType='json', cache=false) {
	$.ajax({
		type: 'GET',
		url: url,
		data: properties,
		dataType: dataType,
		cache: cache,
		success: render
	})
}

function getUlList (sequence) {
	var result = '';
	for (var el = 0; el < sequence.length; el++) {
		result += '<li onclick=\"ajaxRequest(\'' + sequence[el].url +'\', renderObject)\">' + sequence[el].title + '</li>';
	}
	return '<ul>' + result + '</ul>';
}

function renderUlList(data) {
	jQuery(DIV).html(getUlList(data.sequence) + CREATE);
}

function getGoal(goal) {
	return `<h3>${goal.title}</h3><br><h5>${goal.deadline}</h5><br><p>${goal.content}</p>`;
}

function getNote(note) {
	var result = `<h3>${note.date}</h3><hr><h5>${note.time}</h5><p>${note.text}</p><ul>`;
	note.cost_control.forEach((cost) => {result += `<li onclick="">${cost.thing} - ${cost.cost}</li>`;});
	return result + '</ul>';
}

function getObject(data) {
	if (data.status === 'error') {return data.msg;} 
	for (var property in data) {
		switch (property) {
			case 'goal': return getGoal(data.goal); break;
			case 'note': return getNote(data.note); break;
			case 'cost': return getCost(data.cost); break;
			case 'schedule': return getSchedule(data.schedule); break;
		}
	}
}

function renderObject(data) {
	jQuery(DIV).html(getObject(data));
}