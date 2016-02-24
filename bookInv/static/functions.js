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
	bookClicked();
}

function deselectAllBooks() {
	var checks = document.querySelectorAll('input[type="checkbox"]');

	for (var i = 0; i < checks.length; i++) {
		checks[i].checked = false;
	}
	bookClicked();
}

function bookClicked() {
	var num = document.querySelectorAll('input[type="checkbox"]:checked').length;
	var modButton = document.getElementById("modifyBook");
	var delButton = document.getElementById("deleteBook");
	var delLoc = document.getElementById("submitDeleteLocation");

	if (modButton && delButton) {
		if (num === 0) {
			modButton.style.visibility = "hidden";
			modButton.style.opacity = "0";

			delButton.style.visibility = "hidden";
			delButton.style.opacity = "0";

		} else if (num === 1) {
			modButton.style.visibility = "visible";
			modButton.style.opacity = "1";

			delButton.style.visibility = "visible";
			delButton.style.opacity = "1";

		} else if (num > 1) {
			delButton.style.visibility = "visible";
			delButton.style.opacity = "1";

			modButton.style.visibility = "hidden";
			modButton.style.opacity = "0";
		}
	} else {
		if (delLoc.style.visibility === "visible") {
			delLoc.style.visibility = "hidden";
			delLoc.style.opacity = "0";
		} else {
			delLoc.style.visibility = "visible";
			delLoc.style.opacity = "1";
		}
	}
}

function deleteBook() {
	document.getElementById("submitDelete").click();
}

function modifyBook() {
	document.getElementById("submitModify").click();
}
