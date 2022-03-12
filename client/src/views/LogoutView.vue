<template>
  <div>
  </div>
</template>
<script>
import Cookies from 'js-cookie';
export default {
  name: 'LogoutView',
  mounted(){
    ['auth_token'].forEach(cookie => {
      Cookies.remove(cookie);
    })
    window.location.href = '/';
  }
}
</script>