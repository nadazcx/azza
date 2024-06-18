import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, catchError, map, tap, throwError } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://localhost:8000/api'; // Update the base URL as per your backend API
  private Url = 'http://localhost:8000/api/login/'; // Update the base URL as per your backend API


  constructor(private http: HttpClient,private router: Router) {}

  async getToken(): Promise<string | null> {
    try {
      const token = localStorage.getItem('access_token');
      return token;
    } catch (error) {
      console.error('Error fetching token from localStorage:', error);
      return null;
    }
  }
  register(user: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/signup/`, user);
  }

  login(credentials: any) {
    return this.http.post(`${this.Url}`, credentials).pipe(
      map((response: any) => {
        localStorage.setItem('access_token', response.access);
        localStorage.setItem('refresh_token', response.refresh);
        localStorage.setItem('user', JSON.stringify(response.user));
          
          // Store the role of the user
        localStorage.setItem('role', response.role ? 'admin' : 'user');
        return response;
      }),
      catchError(this.handleError)
    );
  }

  logout() {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token')
    localStorage.removeItem('user');
    localStorage.removeItem('role');
    this.router.navigate(['/home']);
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('access_token');
  }

  private handleError(error: any) {
    console.error('API Error:', error);
    return throwError('Something went wrong, please try again later.');
  }

  getHeaders() {
    const token = localStorage.getItem('access_token');
    return new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${token}`
    });
  }

  getRole(): string | null {
    return localStorage.getItem('role');
  }
  getName():string | null{
    return localStorage.getItem('user')
    
  }
}
