<template>
<div>

    <v-card
      color="grey lighten-4"
      flat

      tile
    >
      <v-toolbar extended color="#202C46">

<!--        <v-avatar tile size="90">-->
<!--          <v-img src="@/assets/nstu-logo.jpg"> </v-img>-->
<!--        </v-avatar>-->

<!--        <v-img src="@/assets/nstu-logo.jpg" max-width="100px" max-height="100px"> </v-img>-->

<!--          style="height: 100px; width: 80px;">-->
<!--        <v-icon size="50" class=" pt-11 white&#45;&#45;text" >mdi-book-open-variant</v-icon>-->
        <v-img src="@/assets/ams-icon.png" max-height="60" max-width="60" class="mt-12 ml-16"></v-img>
        <v-toolbar-title class="pt-14 font-weight-bold text-uppercase pl-1" >
          <span class="white--text text-h5">ICE-AMS<br> </span>
          <span class="caption white--text text-capitalize">Smart Attendance Solution for ICE Department</span>

<!--          <span>Noakhali Science &</span> <br> <span>Technology University</span>-->
        </v-toolbar-title>

        <v-spacer></v-spacer>

       <div class="pt-12 white--text">
         <v-btn text class="white--text"> Home </v-btn>
         <v-btn text class="white--text"> About </v-btn>
         <v-btn text class="white--text"> Student </v-btn>
         <v-btn text class="white--text"> Courses </v-btn>
         <v-btn text class="white--text"> Instructor </v-btn>
         <v-btn text class="white--text"> Dashboard </v-btn>
       </div>



      </v-toolbar>
    </v-card>






</div>


</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped></style>
