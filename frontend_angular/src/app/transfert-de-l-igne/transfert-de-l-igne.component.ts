import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { myDataService } from '../mydata.service'; // Adjust the path as needed
import { TransferLigne } from './transfert_ligne.model';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-transfert-de-l-igne',
  templateUrl: './transfert-de-l-igne.component.html',
  styleUrls: ['./transfert-de-l-igne.component.css']
})
export class TRANSFERTDELIGNEComponent implements OnInit {
  transfertLignes: TransferLigne[] = [];
  role: string | null | undefined;
  transfertLigneForm: FormGroup;
  submissionError: string | null = null;

  constructor(
    private myDataService: myDataService,
    private fb: FormBuilder,
    private authService: AuthService
  ) {
    this.transfertLigneForm = this.fb.group({
      numero_de_ligne: ['', Validators.required],
      ancienne_addresse: ['', Validators.required],
      nouvelle_addresse: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    this.role = this.authService.getRole();
    if (this.role === 'admin') {
      this.loadTransferLigne();
    }
  }

  loadTransferLigne() {
    this.myDataService.getTransfertLignes().subscribe(
      data => {
        this.transfertLignes = data;
      },
      error => {
        console.error('Error loading transfert de lignes: ', error);
      }
    );
  }

  addTransfertLigne() {
    console.log('Form submission attempt');
    if (this.transfertLigneForm.valid) {
      console.log('Form is valid. Submitting...');
      this.myDataService.addTransfertLigne(this.transfertLigneForm.value).subscribe(
        () => {
          console.log('Form submitted successfully');
          this.loadTransferLigne();
          this.transfertLigneForm.reset();
          this.submissionError = null;
        },
        error => {
          console.error('Error adding transfert de ligne: ', error);
          this.submissionError = 'Error adding transfert de ligne. Please try again later.';
        }
      );
    } else {
      console.log('Form is invalid');
      this.submissionError = 'Please fill in all required fields.';
    }
  }

  acceptTransfertLigne(transfertLigne: TransferLigne) {
    this.myDataService.accepterTransfertLigne(transfertLigne).subscribe(
      () => {
        this.loadTransferLigne();
      },
      error => {
        console.error('Error accepting transfert de ligne: ', error);
      }
    );
  }

  refuserTransfertLigne(transfertLigne: TransferLigne) {
    this.myDataService.refuserTransfertLigne(transfertLigne).subscribe(
      () => {
        this.loadTransferLigne();
      },
      error => {
        console.error('Error rejecting transfert de ligne: ', error);
      }
    );
  }
}
