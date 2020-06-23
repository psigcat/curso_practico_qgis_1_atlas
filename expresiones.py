
###################### Para añadir imagen 
@project_folder  || '/../Dades/Fanals/Fotos/'
 ||  "id_quadre"  || '.jpg'

 
###################### Para añadir html con imagen
<style>
* {margin: 0px; padding: 0px}
</style>
<img src="[%  'file:///'  || @project_folder || '/../Dades/Fanals/Fotos/' || "id_quadre" ||  '.jpg' %]" 
         width="400" height="300" />

 
###################### Para contar las farolas que contiene cada cuadro de la luz:
# Primero hay que crear una relación en als propiedades del proyecto, con el nomnbre: 
# Relacio_quadres_fanals
relation_aggregate( 
    relation:='Relacio_quadres_fanals', 
    aggregate:='count',
	   expression:="id_quadre")

###################### Otra opción
aggregate(
    layer:='fanals_4da60975_0da9_40ec_94af_b46bfd45488f',
    aggregate:= 'count' ,
    filter:= "id_quadre"= @atlas_pagename ,
    expression:= @atlas_pagename )
