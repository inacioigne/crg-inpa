/*Params*/
const params = new URLSearchParams()
const table = [0,1,2,3,4,5,6,7,8,9]
const fetchAves = (url) => {
    fetch(url)
    .then(response => response.json())
    .then(aves => {
        /*Pagination*/
        records = parseInt(aves.records)
        start = parseInt(aves.start)
        if (start == 0) {
            previous.classList.add('disabled')
            previous.classList.remove('btnActive')
            previous.disabled  = true
        } else {
            previous.classList.remove('disabled')
            previous.classList.add('btnActive')
            previous.disabled  = false
        }
        /*Records*/
        document.getElementById('records').innerHTML = `${aves.records} registros encontrados!`
        if (records == 0) {
            document.getElementById('records').innerHTML = 'Nenhum registro encontrado'
            document.getElementById('table').classList.add("hidden")
        }
        /*Details*/
        exibition = records - start
        if (exibition <= 10) {
            table.slice(exibition).forEach(function(e) {
            document.getElementById('tr-'+e).classList.add("hidden")
            next.classList.remove('btnActive')
            next.classList.add('disabled')
            next.disabled = true
        })} else if (exibition > 10) {
            next.classList.add('btnActive')
            next.classList.remove('disabled')
            next.disabled = false
        }
        aves.response.forEach(function(e, i) {
            document.getElementById('tr-'+i).classList.remove('hidden')
            document.getElementById('cd-'+i).innerHTML = e.codigo
            document.getElementById('sp-'+i).innerHTML = e.especie
            document.getElementById('lc-'+i).innerHTML = e.local
            document.getElementById('dt-'+i).innerHTML = e.data
            document.getElementById("lk-"+i).setAttribute("href", `http://127.0.0.1:5000/detalhespeixes/${e.codigo}`) 
        })
    })
}
const url = `http://127.0.0.1:5000/api/peixes?`
fetchAves(url+params.toString())

/* Filter Searchs */
const search = document.getElementById("search")
const inputSearch = document.getElementById("inputSearch")
const btnSearch = document.getElementById("btnSearch")
btnSearch.addEventListener("click", makeSearch)

function makeSearch(e) {
    if (search.value == 0) {
        alert('Escolha uma categoria!')
    } else {
        for(var key of params.keys()) {
            params.delete(key)
          }
        params.set(search.value, inputSearch.value)
        fetchAves(url+params.toString())
    }
}


/*Filter Dates */
const fromDate = document.getElementById('fromDate')
const toDate = document.getElementById('toDate')
const filter = document.getElementById('filter')
filter.addEventListener("click", filterDate)

function filterDate(e) {
    if (fromDate.value) {
        let date = fromDate.value.split("-")
        let dateFormated = `${date[2]}/${date[1]}/${date[0]}`
        params.set('fromDate', dateFormated)
    }
    if (toDate.value) {
        let date = toDate.value.split("-")
        let dateFormated = `${date[2]}/${date[1]}/${date[0]}`
        params.set('toDate', dateFormated)
    }
    fetchAves(url+params.toString())
}

/*Clean Filter*/
const clean = document.getElementById("clean")
clean.addEventListener("click", function() {document.location.reload(true)})

/*Pagination Functions*/
const next = document.getElementById("next")
const previous = document.getElementById("previous")
next.addEventListener("click", nextPage)
previous.addEventListener("click", previousPage)

function nextPage(e) {
    window.scrollTo(0, 0);
    let offset = start+10
    params.set('offset', offset)
    fetchAves(url+params.toString())
}
function previousPage(e) {
    window.scrollTo(0, 0);
    let offset = start-10
    params.set('offset', offset)
    fetchAves(url+params.toString())
}


