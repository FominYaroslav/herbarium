function validate_form()
{
	valid = true;

        if ((! document.getElementById('search').taxon.value )
	&& (! document.getElementById('search').collector.value )
	&& (! document.getElementById('search').locality.value)
	&& (! document.getElementById('search').barcode.value  )
	&& (! document.getElementById('search').year.value )
	&& (! document.getElementById('search').country.value))
        {
        if(!document.getElementById('al')){
        let div = document.createElement('div');
        div.className = "alert alert-dismissible alert-danger";
        div.id = "al"
        div.innerHTML = '<button type="button\" class=\"close\" data-dismiss=\"alert\">&times;</button>'+
  'Please fill in at least one parement and try  again.';
    document.body.before(div)
}
                valid = false;

}
        return valid;
}