function addBook() {
	var elem = document.getElementById("addBookForm");
	elem.style.top = "10px";
}

function closeBookForm() {
	var elem = document.getElementById("addBookForm");
	elem.style.top = "-900px";
}

function selectAllBooks() {
	var checks = document.querySelectorAll('input[type="checkbox"]');

	for (var i = 0; i < checks.length; i++) {
		checks[i].checked = true;
	}
}

function deselectAllBooks() {
	var checks = document.querySelectorAll('input[type="checkbox"]');

	for (var i = 0; i < checks.length; i++) {
		checks[i].checked = false;
	}
}

function bookClicked() {
	var num = document.querySelectorAll('input[type="checkbox"]:checked').length;
	var modButton = document.getElementById("modifyBook");
	var delButton = document.getElementById("deleteBook");
	var selectAll = document.getElementById("selectAll");
	var deselectAll = document.getElementById("deselectAll");

	if (num == 0) {
		modButton.style.visibility = "hidden";
		modButton.style.opacity = "0";

		delButton.style.visibility = "hidden";
		delButton.style.opacity = "0";

		selectAll.style.display = "none";
		deselectAll.style.display = "none";
	} else if (num == 1) {
		modButton.style.visibility = "visible";
		modButton.style.opacity = "1";

		delButton.style.visibility = "visible";
		delButton.style.opacity = "1";

		selectAll.style.display = "block";
		deselectAll.style.display = "block";
	} else if (num > 1) {
		delButton.style.visibility = "visible";
		delButton.style.opacity = "1";

		modButton.style.visibility = "hidden";
		modButton.style.opacity = "0";

		selectAll.style.display = "block";
		deselectAll.style.display = "block";
	}
}

function deleteBook() {
	document.getElementById("submitDelete").click();
}

function modifyBook() {
	document.getElementById("submitModify").click();
}
