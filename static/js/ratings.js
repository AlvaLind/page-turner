document.addEventListener("DOMContentLoaded", function() {
    const starIcons = document.querySelectorAll(".star-icon");
    const ratingInput = document.getElementById("rating-input");
    const ratingForm = document.getElementById("rating-form");


    // Retrieve the data-value (users rating out of 5) from the stars icons.
    starIcons.forEach(star => {
        star.addEventListener("click", (e) => {
            const ratingValue = e.target.getAttribute("data-value");
            ratingInput.value = ratingValue;

            // Update display by adding class 'rated' to selected star icons.
            starIcons.forEach(icon => {
                if (icon.getAttribute("data-value") <= ratingValue) {
                    icon.classList.add("rated");
                } else {
                    icon.classList.remove("rated");
                }
            });

            // Submit the rating form
            ratingForm.submit();
        });
    });
});
