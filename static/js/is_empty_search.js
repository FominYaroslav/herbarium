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
                alert ( "Пожалуйста заполните хотя бы одно поле поиска." );
                valid = false;
        }

        return valid;
}