import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, throwError } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class GestionMailService {
  private baseUrl = 'http://localhost:8000/gestionmail/'; // Replace with your Django backend URL

  constructor(private http: HttpClient) { }

  // Fetch all emails (for admin view)
  fetchEmails(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}emails/`)
      .pipe(
        catchError(this.handleError)
      );
  }

  // Create a new email
  createEmail(emailData: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}emails/`, emailData)
      .pipe(
        catchError(this.handleError)
      );
  }
  getEmailById(): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}getId/`)
      .pipe(
        catchError(this.handleError)
      );
  }

  
  acceptEmail(emailId: number): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}${emailId}/accept/`, {})
      .pipe(
        catchError(this.handleError)
      );
  }

  refuseEmail(emailId: number): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}${emailId}/refuse/`, {})
      .pipe(
        catchError(this.handleError)
      );
  }

  // Handle errors
  private handleError(error: any) {
    console.error('API Error:', error);
    return throwError('Something went wrong, please try again later.');
  }
}