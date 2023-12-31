//      footer
        document.addEventListener("DOMContentLoaded", function() {
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
        document.addEventListener("DOMContentLoaded", function() {
            var scrollToTopBtn = document.getElementById("scrollToTopBtn");

            window.addEventListener("scroll", function() {
                if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
                    scrollToTopBtn.style.display = "block";
                } else {
                    scrollToTopBtn.style.display = "none";
                }
            });

            scrollToTopBtn.addEventListener("click", function() {
                scrollToTop();
            });

            function scrollToTop() {
                var element = document.documentElement;
                element.scrollIntoView({
                    behavior: "smooth"
                });
            }
        });