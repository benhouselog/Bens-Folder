function toggleMenu() {
    if (document.getElementById("main-nav").style.right == "0px") {
        var numChildren = document.getElementById("main-nav").childNodes.length;
        document.getElementById("main-nav").style.right = "50vw";
        document.getElementById("burger").classList.add("open");
    } else {
        document.getElementById("main-nav").style.right = "0px";
        document.getElementById("burger").classList.remove("open");
    }
}
