<script setup>
defineProps({
  msg: {
    type: String,
    required: false
  }
})
</script>

<template>
 <!-- Navbar Start -->
 <div class="container-fluid bg-white sticky-top">
        <div class="container">
            <nav class="navbar navbar-expand-lg bg-white navbar-light p-lg-0">
                <a href="index.html" class="navbar-brand d-lg-none">
                    <img src="img/logo/logo.png" class="m-0" width="70">
                </a>
                <button type="button" class="navbar-toggler me-0" data-bs-toggle="collapse"
                    data-bs-target="#navbarCollapse">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarCollapse">
                    
                    <div class="navbar-nav d-lg-flex justify-content-between">
                        <div class="col-lg-2 d-none d-lg-flex justify-content-lg-start ms-0 align-items-center">
                            <a href="index.html" class="navbar-brand ">
                                <img src="img/logo/logo.png" width="60">
                                
                            </a>
                        </div>
                        <div class="col-md-3 d-lg-flex justify-content-between">
                            <a href="index.html" class="nav-item nav-link active text-center">Home</a>
                            <a href="about.html" class="nav-item nav-link text-center">About</a>
                            <a href="service.html" class="nav-item nav-link text-center">Services</a>
                           
                            <a href="contact.html" class="nav-item nav-link text-center">Contact</a>
                        </div>
                        
                    </div>
                   
                </div>
            </nav>
        </div>
    </div>
    <!-- Navbar End -->

</template>
