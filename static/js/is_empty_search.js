function validate_form()
{
	valid = true;

        if ((! document.getElementById('search').taxon.value )
	&& (! document.getElementById('search').genus.value )
	&& (! document.getElementById('search').locality.value)
	&& (! document.getElementById('search').barcode.value  )
	&& (! document.getElementById('search').species.value )
	&& (! document.getElementById('search').country.value))
        {
                alert ( "Пожалуйста заполните хотя бы одно поле поиска." );
                valid = false;
        }

        return valid;
}