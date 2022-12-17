function eliminar_usuario(x) {
    id_usuario=x.value;
    form_eliminar=document.getElementById ("form_eliminar").action="/adm/usuario-eliminar/"+id_usuario+"/";

}

function ejecutar_eliminarf() {
    document.getElementById ("form_eliminar").submit();

}


/*
#hmtl
<button type="button" id="edito" className="btn btn-outline-secondary" data-toggle="modal" data-target="#editarempleado"
        data-stuff='["{{r.id}}", "{{r.nombre}}" , "{{r.apellidos}}", "{{r.direccion}}", "{{r.cargo}}","{{r.telefono}}","{{r.celular}}" ,"{{r.fechaingreso|date("Y-m-d")}}", "{{r.salario}}" , "{{r.pcomision}}", "{{r.password}}"]'>
    <i className="fa fa-user-plus"></i> Editar</button>

mio
<button type="form" id="edito" className="btn btn-outline-secondary" data-toggle="modal" data-target="#editarusuario"
        data-stuff='["{{r.id}}", "{{r.nombre}}" , "{{r.apellidos}}", "{{r.direccion}}", "{{r.cargo}}","{{r.telefono}}","{{r.celular}}" ,"{{r.fechaingreso|date("Y-m-d")}}", "{{r.salario}}" , "{{r.pcomision}}", "{{r.password}}"]'>
    <i className="fa fa-user-plus"></i> Editar</button>

#js
     $("#editarusuario").on('show.bs.modal', function (event) {
      var button = $(event.relatedTarget);

      var vars = button.data('stuff');

      $('#edit_empleado_id').val(vars[0]);
      $('#edit_empleado_nombre').val(vars[1]);
      $('#edit_empleado_apellidos').val(vars[2]);
      $('#edit_empleado_direccion').val(vars[3]);
      $('#edit_empleado_cargo').val(vars[4]);
      $('#edit_empleado_telf').val(vars[5]);
      $('#edit_empleado_cel').val(vars[6]);
      $('#edit_empleado_feingreso').val(vars[7]);
      $('#edit_empleado_salario').val(vars[8]);
      $('#edit_empleado_comision').val(vars[9]);
      $('#edit_empleado_password').val(vars[10]);

  });

html



#js

para tabla cuando se ingresan datos secundarios de bobivos

function agregarCarrito(x) {
    id_prod = x.id;
    formulario = document.getElementById('form-carrito');
    formulario.action='/Tienda/agregarProductoCarrito/'+id_prod+'/';
    document.getElementById('cantidadDeseada').max=x.value;





 */