import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, switchMap } from 'rxjs/operators';
import { Reclamation } from "./reclamations/reclamation.model"
import { Suggestion } from './suggestions/suggestions.model';
import { AuthService } from './auth.service';
import { MigrationOffre } from './migration-d-offre/migration-d-offre.model';

@Injectable({
  providedIn: 'root'
})
export class myDataService  {
  private apiUrl = 'http://localhost:8000/factures/factures/';
  private Url = 'http://localhost:8000/api/getId/';
  private reclamationUrl = 'http://localhost:8000/reclamation/reclamations/';
  private suggestionUrl = 'http://localhost:8000/suggestion/suggestions/';
  private transfertLigneUrl = 'http://localhost:8000/transfer/transfer-lignes/';
  private migrationOffreUrl = 'http://localhost:8000/migration_offre/migration-offres/';
  

  
  constructor(private http: HttpClient,private authService : AuthService) { }
  getId():Observable<any>{
    const token = localStorage.getItem('access_token');
    
    
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + token
    });
    console.log('headers is',headers);
    
    return this.http.get(this.Url,{ headers: headers })
  }
  getFactures(): Observable<any> {
    return this.http.get(this.apiUrl);
  }

  getFacture(): Observable<any> {
    const token = localStorage.getItem('access_token');
    
    
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + token
    });
    return this.getId().pipe(
      switchMap(response => {
        const userId = response.user_id; // Adjust according to your API response structure
        return this.http.get(`${this.apiUrl}`,{headers});
      })
    );
  }

  createFacture(facture: any): Observable<any> {
    const token = localStorage.getItem('access_token');
    
    
    const headers = new HttpHeaders({
      'Authorization': 'Bearer ' + token
    });
    return this.http.post(this.apiUrl, facture, { headers });
  }

  private getHeaders(): HttpHeaders {
    const accessToken = localStorage.getItem('access_token');
    return new HttpHeaders({ 'Authorization': `Bearer ${accessToken}` });
  }

  getReclamations(): Observable<Reclamation[]> {
    return this.http.get<Reclamation[]>(this.reclamationUrl, { headers: this.getHeaders() }).pipe(
      catchError(error => {
        console.error('Error getting reclamations: ', error);
        return throwError(error);
      })
    );
  }

  acceptReclamation(reclamation: Reclamation): Observable<any> {
    const acceptUrl = `${this.reclamationUrl}${reclamation.id}/accepter_reclamation/`;
    return this.http.post(acceptUrl, reclamation, { headers: this.getHeaders() }).pipe(
      catchError(error => {
        console.error('Error accepting reclamation: ', error);
        return throwError(error);
      })
    );
  }

  refuserReclamation(reclamation: Reclamation): Observable<any> {
    const refuserUrl = `${this.reclamationUrl}${reclamation.id}/refuser_reclamation/`;
    return this.http.post(refuserUrl, reclamation, { headers: this.getHeaders() }).pipe(
      catchError(error => {
        console.error('Error refusing reclamation: ', error);
        return throwError(error);
      })
    );
  }

  ajouterReclamation(reclamation: Reclamation): Observable<any> {
    return this.http.post(this.reclamationUrl, reclamation, { headers: this.getHeaders() }).pipe(
      catchError(error => {
        console.error('Error adding reclamation: ', error);
        return throwError(error);
      })
    );
  }

  getSuggestions(): Observable<Suggestion[]> {
    return this.http.get<Suggestion[]>(this.suggestionUrl, { headers: this.getHeaders() });
  }

  addSuggestion(suggestion: Suggestion): Observable<any> {
    return this.http.post(this.suggestionUrl, suggestion, { headers: this.getHeaders() });
  }

  acceptSuggestion(suggestion: Suggestion): Observable<any> {
    const acceptUrl = `${this.suggestionUrl}${suggestion.id}/accepter_suggestion/`;
    return this.http.post(acceptUrl, suggestion, { headers: this.getHeaders() });
  }

  rejectSuggestion(suggestion: Suggestion): Observable<any> {
    const rejectUrl = `${this.suggestionUrl}${suggestion.id}/refuser_suggestion/`;
    return this.http.post(rejectUrl, suggestion, { headers: this.getHeaders() });
  }
  getTransfertLignes(): Observable<any> {
    return this.http.get<Suggestion[]>(this.transfertLigneUrl, { headers: this.getHeaders() });
  }
  addTransfertLigne(transfertLigne: any): Observable<any> {
    return this.http.post(this.transfertLigneUrl, transfertLigne, { headers: this.getHeaders() });
  }
  accepterTransfertLigne(transfertLigne: any): Observable<any> {
    const acceptUrl = `${this.transfertLigneUrl}${transfertLigne.id}/accepter_demande/`;
    return this.http.post(acceptUrl, transfertLigne, { headers: this.getHeaders() });
  }
  refuserTransfertLigne(transfertLigne: any): Observable<any> {
    const rejectUrl = `${this.transfertLigneUrl}${transfertLigne.id}/refuser_demande/`;
    return this.http.post(rejectUrl, transfertLigne, { headers: this.getHeaders() });
  }
  createMigrationOffre(migrationOffre: MigrationOffre): Observable<any> {
    const headers = this.getHeaders();
    return this.http.post(this.migrationOffreUrl, migrationOffre, { headers });
  }
  accepterMigrationOffre(offreId: number): Observable<any> {
    const accepterUrl = `${this.migrationOffreUrl}${offreId}/accepter_offre/`;
    const headers = this.getHeaders();
    return this.http.post(accepterUrl, {}, { headers });
  }

  refuserMigrationOffre(offreId: number): Observable<any> {
    const refuserUrl = `${this.migrationOffreUrl}${offreId}/refuser_offre/`;
    const headers = this.getHeaders();
    return this.http.post(refuserUrl, {}, { headers });
  }
  getMigrationOffres(): Observable<MigrationOffre[]> {
    const headers = this.getHeaders();
    return this.http.get<MigrationOffre[]>(this.migrationOffreUrl, { headers }).pipe(
      catchError(error => {
        console.error('Error getting migration offres: ', error);
        return throwError(error);
      })
    );
  }

}
