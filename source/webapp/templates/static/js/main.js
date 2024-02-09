async function makeRequest(url, method = 'GET'){
    let response = await fetch(url, {method});
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;
    }
}

    async function onClick (e) {
        e.preventDefault();
        let a = e.target.closest('a');
        let url = a.href;
        let response = await makeRequest(url);
        if (a.innerText === '<i class="bi bi-heart"></i>'){
            a.innerText = '<i class="bi bi-heart-fill"></i>';
        } else {
            a.innerText = '<i class="bi bi-heart"></i>';
        }
        let span = document.getElementById(a.dataset['spanCountId'])
        span.innerText = response.count;
    }

    async function onLoad () {
        let likes = document.getElementsByClassName('likes');
        for (let like of likes) {
            like.addEventListener('click', onClick)
        }
    }

    window.addEventListener('load', onLoad)