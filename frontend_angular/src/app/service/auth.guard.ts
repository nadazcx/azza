import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree } from '@angular/router';
import { AuthService } from '../auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {

  constructor(private authService: AuthService, private router: Router) {}

  async canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Promise<boolean | UrlTree> {
    
    const isAuthenticated = await this.authService.getToken() !== null;

    if (!isAuthenticated) {
      this.router.navigate(['/home']);
      return false;
    }

    const role = this.authService.getRole();
    const expectedRole = route.data['expectedRole'];  // Get the expected role from route data

    if (expectedRole && role !== expectedRole) {
      this.router.navigate(['/home']);  // Redirect to a forbidden page or home
      return false;
    }

    return true;
  }
}
