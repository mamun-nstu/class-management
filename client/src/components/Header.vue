<template>

    <nav>
      <div class="g-signin2" data-onsuccess="onSignIn"></div>
      <v-toolbar app height="130" class="flat">

        <v-img src="@/assets/nstu-logo.png" max-height="130px" max-width="100px"></v-img>

        <v-toolbar-title class="pl-2 indigo--text font-weight-bold text--darken-4 text-h5">Noakhali Science & Technology University</v-toolbar-title>

      <v-spacer></v-spacer>


        <v-btn text color="black" class="px-10 mt-16">
          Home
        </v-btn>
        <v-btn text color="black" class=" mt-16">
          About
        </v-btn><v-btn text color="black" class=" mt-16">
          Students
        </v-btn><v-btn text color="black" class="mt-16">
          Courses
        </v-btn><v-btn text color="black" class=" mt-16">
          Attendances
        </v-btn>
        <v-btn text color="black" class=" pr-3 mt-16">
          Instructor
        </v-btn><v-btn text color="black" class=" pr-3 mt-16">
          Dashboard
        </v-btn>

    </v-toolbar>
  </nav>


</template>

<script>
export default {
  name: "Header",
};
</script>

<style scoped></style>
