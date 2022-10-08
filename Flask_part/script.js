function toggle(source) {
    checkboxes = document.getElementsByName('health');
    for(var i=0, n=checkboxes.length;i<n;i++) {
      checkboxes[i].checked = source.checked;
    }
    }

$('#iframe_').load(document.URL +  ' #iframe_
