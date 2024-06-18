

import { Injectable } from '@angular/core';
import { CanActivate, Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Injectable({
  providedIn: 'root'
})
export class adminAuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) { }

  canActivate(): boolean {
    const role = this.authService.getRole();
    if (role === 'admin') {
      return true;
    } else {
      this.router.navigate(['/home']);  // Redirect to a forbidden page or home
      return false;
    }
  }
}
