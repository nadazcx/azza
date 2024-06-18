import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent {
  registerForm: FormGroup;
  loginForm : FormGroup;
  
  constructor(private fb: FormBuilder, private http: HttpClient,private router: Router,private authService : AuthService) {
    this.registerForm = this.fb.group({
      cin: ['', Validators.required],
      name: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      confirmPassword: ['', Validators.required],
      role: ['user', Validators.required]
    });

    this.loginForm = this.fb.group({
      // Define your form controls and validators here
      email: ['', [Validators.required, Validators.email]],
      password: ['', Validators.required],
      // Add other form controls as needed
    });
  }

  

  onRegisterSubmit() {
    if (this.registerForm.valid) {
      this.authService.register(this.registerForm.value).subscribe(
        response => {
          console.log('User registered successfully', response);
          this.router.navigate(['/home']);
        },
        error => {
          console.error('There was an error during the request', error);
        }
      );
    }
  }

  login() {
    if (this.loginForm.valid) {
      
      this.authService.login(this.loginForm.value).subscribe(
        response => {
          console.log('Login successful', response);
          this.router.navigate(['/welcome'])
        },
        error => {
          console.log(this.loginForm.value);
          
          console.error('Login error', error);
          // Handle login error (display error message, etc.)
        }
      );
    }
  }
  

  
 

 
}
