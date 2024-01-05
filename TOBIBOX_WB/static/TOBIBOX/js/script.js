//      footer
document.addEventListener("DOMContentLoaded", function () {
    var footer = document.getElementById("footer");
    var main = document.querySelector("main");

    function isScrolledToBottom() {
        return window.innerHeight + window.scrollY >= document.body.offsetHeight;
    }

    function checkFooterVisibility() {
        if (isScrolledToBottom()) {
            footer.classList.add("show");
        } else {
            footer.classList.remove("show");
        }
    }

    window.addEventListener("scroll", checkFooterVisibility);
    window.addEventListener("resize", checkFooterVisibility);
    window.addEventListener("DOMContentLoaded", checkFooterVisibility);
});

//      scroll 
document.addEventListener("DOMContentLoaded", function () {
    var scrollToTopBtn = document.getElementById("scrollToTopBtn");

    window.addEventListener("scroll", function () {
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            scrollToTopBtn.style.display = "block";
        } else {
            scrollToTopBtn.style.display = "none";
        }
    });

    scrollToTopBtn.addEventListener("click", function () {
        scrollToTop();
    });

    function scrollToTop() {
        var element = document.documentElement;
        element.scrollIntoView({
            behavior: "smooth"
        });
    }
});

var cleancer = true;

function clearFields() {
    // Очистка всех полей формы
    document.getElementsByName("width")[0].value = "";
    document.getElementsByName("height")[0].value = "";
    document.getElementsByName("depth")[0].value = "";
    document.getElementsByName("material")[0].value = "";
}

function validateForm() {
    var width = document.getElementsByName('width')[0].value;
    var height = document.getElementsByName('height')[0].value;
    var depth = document.getElementsByName('depth')[0].value;
    var material = document.getElementsByName('material')[0].value;
    
    
    if (width === "" || height === "" || depth === "" || material === "") {
        alert("Будь ласка, заповніть усі поля!"); // More informative error message
        cleancer = false;
        return false;
    }
    
    cleancer = true;
    return true; 
    
}

function submitFormWithDelay() {
    if (cleancer) {
        setTimeout(function () {
            clearFields();
            cleancer = false;
        }, 2000);
    }
}