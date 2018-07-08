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
	result = '';
	for (var el = 0; el < sequence.length; el++) {
		result += '<li><button type="submit" onclik=\"ajaxRequest(\'' + sequence[el][2] +'\', renderObject)\">' + sequence[el][1] + '</button></li>';
	}
	return '<ul>' + result + '</ul>';
}

function renderUlList(data) {
	jQuery(DIV).html(getUlList(data.sequence) + CREATE);
}

function getObject(object) {
	return object;
}

function renderObject(data) {
	jQuery(DIV).html(JSON.stringify(data));
}