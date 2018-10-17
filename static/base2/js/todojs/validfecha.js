function isValidDate(day, month, year) {
  var dteDate;

  month = month - 1;
  dteDate = new Date(year, month, day);

  return ((day == dteDate.getDate()) && (month == dteDate.getMonth()) && (year == dteDate.getFullYear()));
}

function validate_fecha(fecha) {
  var patron = new RegExp('^(19|20)+([0-9]{2})([-])([0-9]{1,2})([-])([0-9]{1,2})$');

  if(fecha.search(patron) == 0) {
    var values = fecha.split('-');

    if(isValidDate(values[2],values[1],values[0])) {
      return true;
    }
  }
  return false;
}

function Edad() {
  var fecha = document.getElementById('id_fecha_naci').value;
  var edad = document.getElementById('id_edad').value;

  if(validate_fecha(fecha) == true) {
    var values = fecha.split('-');
    var dia = values[2];
    var mes = values[1];
    var ano = values[0];

    var fecha_hoy = new Date();
    var ahora_ano = fecha_hoy.getYear();
    var ahora_mes = fecha_hoy.getMonth() + 1;
    var ahora_dia = fecha_hoy.getDate();

    var edad = (ahora_ano + 1900) - ano;

    if(ahora_mes < mes) {
      edad--;
    }

    if((mes == ahora_mes) && (ahora_dia < dia)) {
      edad--;
    }

    if(edad > 1900) {
      edad -= 1900;
    }

    var meses = 0;

    if(ahora_mes > mes)
      meses = ahora_mes - mes;
    if(ahora_mes < mes)
      meses = 12 - (mes - ahora_mes);
    if(ahora_mes == mes && dia > ahora_dia)
      meses = 11;

    var dias = 0;
    if(ahora_dia > dia)
      dias = ahora_dia - dia;
    if(ahora_dia < dia) {
      ultimoDiaMes = new Date(ahora_ano, ahora_mes, 0);
      dias = ultimoDiaMes.getDate() - (dia - ahora_dia);
    }

    document.getElementById('id_edad').value = edad
  } else {
    $('#alertaDos').html('La fecha ' + fecha + ' Es incorrecta...').slideDown(150000);
    $('#id_fecha_naci').val('');
    $('#id_edad').val('');
    $('#id_fecha_naci').focus();
    return false;
  }

  if(edad <= 17) {
    $('#alertaDos').html('Usted tiene '+ edad + ' años de edad por lo tanto, ¡NO Puede Ser Registrado!').slideDown(15);
    $('#id_edad').val('');
    $('#id_fecha_naci').val('');
    $('#id_fecha_naci').focus();
    return false;
  }
  else {
    $('#alertaDos').addClass('hidden')
  }
}
