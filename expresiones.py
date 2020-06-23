
# Para añadir imagen 
@project_folder  || '/../Dades/Fanals/Fotos/'
 ||  "id_quadre"  || '.jpg'

 
 # Para añadir html con imagen
 <style>
* {margin: 0px; padding: 0px}
</style>
<img src="[%  'file:///'  || @project_folder || '/../Dades/Fanals/Fotos/' || "id_quadre" ||  '.jpg' %]" 
         width="400" height="300" />
