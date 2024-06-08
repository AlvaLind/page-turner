document.addEventListener('DOMContentLoaded', function () {
    // Select all star icons and current user rating element
    const stars = document.querySelectorAll('.star-icon');
    const userRating = document.getElementById('user-rating');

    // Attach event listeners to each star
    stars.forEach(star => {
        star.addEventListener('mouseover', handleStarHover);
        star.addEventListener('mouseout', handleStarHoverOut);
        star.addEventListener('click', handleStarClick);
    });

    ```
        Function to handle star hover event
        Gets the hovered star value and fills all stars 
        up to that star while mouse is hovering over it.
    ```
    function handleStarHover(event) {
        const value = event.target.getAttribute('data-value');
        fillStars(value);
    }

    ``` 
        Function to handle mouseout event
        Fills stars up to the user's last submitted rating
    ```
    function handleStarHoverOut() {
        fillStars(userRating.textContent);
    }

    ```
        Function to handle star click event
        Finds the closest form containing the clicked star
        gets the data-value from the clicked star
        updates the user rating
        fills stars up to and including the clicked star
        and then submits the form via AJAX 

    ```
    function handleStarClick(event) {
        event.preventDefault(); // Prevent the default form submission 
        const form = event.target.closest('form');
        const value = event.target.getAttribute('data-value');
        userRating.textContent = value;
        fillStars(value);
        submitForm(form, value); // Submit the form via AJAX not default
    }

    ```
        Function to colour/fill star icons up to a given data-value 
        iterates over for each star icon
        Adds 'filled' class to stars with data-value <= the value arg
        otherwise remove the 'filled' class
        'filled' class in styles changes star colour to yellow
    ```
    function fillStars(value) {
        stars.forEach(star => {
            if (star.getAttribute('data-value') <= value) {
                star.classList.add('filled');
            } else {
                star.classList.remove('filled');
            }
        });
    }

    ```
        Function to submit the form via AJAX in order
        to submit the rating form data to the server without
        reloading the entire webpage.
        Creates FormData object from the form 
        Sets the rating value in the FormData object
    ```
    function submitForm(form, value) {
        const formData = new FormData(form);
        formData.set('rating', value); 

        // Send a fetch request to the form action 
        fetch(form.action, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            }
        })
    }

    // Colour/fill the stars based on the user's existing rating
    fillStars(userRating.textContent);
});
