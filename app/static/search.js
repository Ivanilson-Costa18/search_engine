document.getElementById('searchbox').addEventListener('keyup', async (e) => {
    let autocompleteDiv = document.getElementById('autocomplete')
    let suggestionsDiv = document.querySelector('.suggestions')
    let searchformForm = document.getElementById("searchform")
    try {
        let response = await fetch(`/suggestions?q=${e.target.value}`)
        let result = await response.json()

        if(result.suggestions.length === 0){
            autocompleteDiv.style.display = 'none'
            searchformForm.classList.remove('autocomplete-active')
            return;
        }


        let html = ""
        for(let suggestion of result.suggestions){
            let button = 
            `<button type="button" class="suggestion">
                <div class="suggestion-wrapper">
                    <div class="icon-wrapper">
                        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" class="icon" viewBox="0 0 24 24">
                            <path fill-rule="evenodd" d="M10.498 2a8.498 8.498 0 1 0 5.843 14.67l4.292 4.291a.8.8 0 1 0 1.131-1.13l-4.367-4.368A8.498 8.498 0 0 0 10.499 2M3.6 10.498a6.898 6.898 0 1 1 13.797 0 6.898 6.898 0 0 1-13.797 0" clip-rule="evenodd"></path>
                        </svg>
                    </div>
                    <span class="suggestion-text">${suggestion}</span>
                </div>
            </button>`
            html += button
        }

        suggestionsDiv.innerHTML = html
        autocompleteDiv.style.display = 'block'
        searchformForm.classList.add('autocomplete-active')
        updateDOM()
        return;
    } catch (error) {
        return error
    }
})

const updateDOM = () => {
    const search = e => {
        console.log('click')
        let spanContent = e.target.querySelector('.suggestion-text');
        let text = spanContent.textContent
        window.location = `/search?q=${text}`
    }
    
    document.querySelectorAll('.suggestion').forEach(button => {
        button.addEventListener('click', search)
    })
}
