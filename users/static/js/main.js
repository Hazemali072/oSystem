function down() {
	document.getElementById("myDropdown").classList.toggle("show");
}

window.onclick = function (event) {
	if (!event.target.matches('.dropbtn')) {
		var dropdowns = document.getElementsByClassName("dropdown-content");
		var i;
		for (i = 0; i < dropdowns.length; i++) {
			var openDropdown = dropdowns[i];
			if (openDropdown.classList.contains('show')) {
				openDropdown.classList.remove('show');
			}
		}
	}
};

$('.ev-popup').magnificPopup({
	type: 'inline',
	closeOnContentClick: false,
	midClick: true,
	callbacks: {
		beforeOpen: function () {
			'use strict'
			this.st.mainClass = this.st.el.attr('data-effect');
		}
	},
	zoom: {
		enabled: true,
		duration: 500,
	},
	mainClass: 'mfp-fade',
});

function CopyToClipboard(containerid) {
	'use strict'
	if (document.selection) {
		var range = document.body.createTextRange();
		range.moveToElementText(document.getElementById(containerid));
		range.select().createTextRange();
		document.execCommand("copy");
	} else if (window.getSelection) {
		var range = document.createRange();
		range.selectNode(document.getElementById(containerid));
		window.getSelection().addRange(range);
		document.execCommand("copy");
	}
}

var addBtn = document.getElementById('c-btn');
var modalBg = document.getElementById('modal-bg');
var modalClose = document.getElementById('modal-close');
var evBtn = document.getElementById('ev-btn');
var tBtn = document.getElementById('t-btn');

addBtn.addEventListener('click', function () {
	'use strict'
	modalBg.classList.add('active-modal');
});
modalClose.addEventListener('click', function () {
	'use strict'
	modalBg.classList.remove('active-modal');
});
evBtn.addEventListener('click', function () {
	'use strict'
	modalBg.classList.remove('active-modal');
});
tBtn.addEventListener('click', function () {
	'use strict'
	modalBg.classList.remove('active-modal');
});


function openSec(evt, secName) {
	var i, tabcontent, tablinks;
	tabcontent = document.getElementsByClassName("tabcontent");
	for (i = 0; i < tabcontent.length; i++) {
		tabcontent[i].style.display = "none";
	}
	tablinks = document.getElementsByClassName("tablinks");
	for (i = 0; i < tablinks.length; i++) {
		tablinks[i].className = tablinks[i].className.replace(" active-btn ", " ");
	}
	document.getElementById(secName).style.display = "block";
	evt.currentTarget.className += " active-btn ";
};

var rBtn = document.getElementById('r-btn');
var rModal = document.getElementById('modal-bg-r');
var rClose = document.getElementById('modal-close-r');

rBtn.addEventListener('click', function () {
	rModal.classList.add('active-modal')
});
rClose.addEventListener('click', function () {
	rModal.classList.remove('active-modal');
});

new ClipboardJS('.btn-c');

var rellax = new Rellax('.rellax');

new ClipboardJS('.btn-copy');

new WOW().init();

//$(function() {  
//    $(".c-tables").niceScroll({
//		cursorcolor: "#424242",
//		scrollspeed: 60,
//		cursorwidth: "5px",
//		cursorborder: "1px solid #fff", 
//	});
//});
