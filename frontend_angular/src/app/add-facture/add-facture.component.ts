// add-facture.component.ts
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';

import { AuthService } from '../auth.service';
import { Router } from '@angular/router';
import { myDataService } from '../mydata.service';

@Component({
  selector: 'app-add-facture',
  templateUrl: './add-facture.component.html',
  styleUrls: ['./add-facture.component.css']
})
export class AddFactureComponent implements OnInit {
  factureForm: FormGroup;
  role: string | null;
  factures: any[] = []; // Assuming you'll fetch JSON objects from backend
  selectedFacture: any | null = null; // Adjust this based on your backend response structure
  user : any | null={}
  constructor(
    private fb: FormBuilder,
    private dataService: myDataService,
    private authService: AuthService,
    private router: Router
  ) {
    this.factureForm = this.fb.group({
      numero: '',
      date_emission: '',
      client: '',
      montant: '',
      description: ''
    });
    this.role = '';
    console.log(this.loadName());
    this.user = this.loadName();
  }

  ngOnInit(): void {
    this.role = this.authService.getRole();
    if (this.role === 'user') {
      this.loadFactures();
    }
    this.role = this.authService.getRole();
  }

  loadFactures() {
    this.dataService.getFacture().subscribe(
      (factures) => {
        this.factures = factures;
        
      },
      (error) => {
        console.error('Failed to load factures', error);
      }
    );
  }
  loadName(){
    return this.authService.getName()
  }
  onSubmit() {
    if (this.factureForm.valid) {
      console.log(this.factureForm.value);
      
      this.dataService.createFacture(this.factureForm.value).subscribe(
        (response) => {
          console.log('Facture created', response);
          // Optionally, reset the form or provide feedback to the user
          this.router.navigate(['/factures', response.id]); // Example navigation to detail page
        },
        (error) => {
          console.error('Failed to create facture', error);
        }
      );
    }
  }

  selectFacture(facture: any) {
    this.selectedFacture = facture;
  }

  onSaveAndAddAnother() {
    if (this.factureForm.valid) {
      this.dataService.createFacture(this.factureForm.value).subscribe(
        (response) => {
          console.log('Facture created', response);
          this.factureForm.reset(); // Reset the form for new entry
        },
        (error) => {
          console.error('Failed to create facture', error);
        }
      );
    }
  }

  onSaveAndContinueEditing() {
    if (this.factureForm.valid) {
      this.dataService.createFacture(this.factureForm.value).subscribe(
        (response) => {
          console.log('Facture created', response);
          this.router.navigate(['/factures', response.id, 'edit']); // Navigate to edit page
        },
        (error) => {
          console.error('Failed to create facture', error);
        }
      );
    }
  }
}
