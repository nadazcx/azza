import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent {
  constructor(private router: Router,private authService : AuthService) {}
  navigateTohome() {
    this.router.navigate(['/home']);
  }
  logout(){
    this.authService.logout();
  }
}
