import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../../../core/auth.service';
import { Router, Params } from '@angular/router';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Meta } from '@angular/platform-browser';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginForm: FormGroup;
  errorMessage: string = '';
  successMessage: string = '';

  constructor(
    private meta: Meta,
    public authService: AuthService,
    private router: Router,
    private fb: FormBuilder
  ) { 
    meta.addTag({name: 'viewport', content: 'width=device-width, initial-scale=1'});
    this.createForm();
  }

  createForm() {
    this.loginForm = this.fb.group({
      email: ['', Validators.required ],
      password: ['', Validators.required]
    });
  }

  tryLogin(value){
    this.authService.doLogin(value)
    .then(res => {
      console.log(res);
      this.errorMessage = "";
      this.successMessage = "You are logged in";
      this.router.navigate(['/dashboard']);
    }, err => {
      console.log(err);
      this.successMessage = "";
      this.errorMessage = err.message;
    })
  }

  ngOnInit() {
  }

}
