import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import { myDataService  } from '../mydata.service';
import { Reclamation } from './reclamation.model';

@Component({
  selector: 'app-reclamations',
  templateUrl: './reclamations.component.html',
  styleUrls: ['./reclamations.component.css']
})
export class RECLAMATIONSComponent implements OnInit {
  reclamations: Reclamation[] = [];
  role: string | null;
  reclamationForm: FormGroup;

  constructor(
    private myDataService: myDataService ,
    private fb: FormBuilder,
    private authService: AuthService
  ) {
    this.role = '';
    this.reclamationForm = this.fb.group({
      numero: ['', Validators.required],
      sujet: ['', Validators.required],
      description: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    this.role = this.authService.getRole();
    if (this.role === 'admin') {
      this.loadReclamations();
    }
  }

  loadReclamations() {
    this.myDataService.getReclamations().subscribe(
      data => {
        this.reclamations = data;
      },
      error => {
        console.error('Error loading reclamations: ', error);
      }
    );
  }

  accepterReclamation(reclamation: Reclamation) {
    this.myDataService.acceptReclamation(reclamation).subscribe(
      () => {
        this.loadReclamations();
      },
      error => {
        console.error('Error accepting reclamation: ', error);
      }
    );
  }

  refuserReclamation(reclamation: Reclamation) {
    this.myDataService.refuserReclamation(reclamation).subscribe(
      () => {
        this.loadReclamations();
      },
      error => {
        console.error('Error refusing reclamation: ', error);
      }
    );
  }

  ajouterReclamation() {
    if (this.reclamationForm.valid) {
      const { numero, sujet, description } = this.reclamationForm.value;
      const newReclamation: Reclamation = {
        numero, sujet, description,
      }; 
      this.myDataService.ajouterReclamation(newReclamation).subscribe(
        () => {
          this.loadReclamations();
          this.reclamationForm.reset();
        },
        error => {
          console.error('Error adding reclamation: ', error);
        }
      );
    } else {
      console.error('Form is invalid. Cannot submit.');
    }
   }
}
