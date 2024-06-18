import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import { myDataService } from '../mydata.service';
import { Router } from '@angular/router';
import { GestionMailService } from '../gestion-mail.service';

@Component({
  selector: 'app-gestion-emails',
  templateUrl: './gestion-emails.component.html',
  styleUrls: ['./gestion-emails.component.css']
})
export class GestionEmailsComponent implements OnInit {
  role: string | null; // Will be determined by AuthService
  emailsForm: FormGroup;
  emails: any[] = [];
  emailId : any
  constructor(private fb: FormBuilder,
    private dataService: myDataService,
    private authService: AuthService,
    private router: Router,
    private emailService : GestionMailService) {
    this.role=''
    this.emailsForm = this.fb.group({
      addresse: '',
      emailRecuperation: '',
      messages: '',
      status: '',
      adminResulat:'pending'
      
    });
    this.emailId = this.getId()
   }

   ngOnInit(): void {
    this.role = this.authService.getRole();
    if (this.role === 'admin') {
      this.fetchEmails();
    }
  }

  onSubmit() {
    if (this.role === 'user') {
      const formData = this.emailsForm.value;
      this.emailService.createEmail(formData)
        .subscribe(response => {
          console.log('Email saved successfully:', response);
          // Optionally, reset form or show success message
        }, error => {
          console.error('Error saving email:', error);
          // Handle error (show error message or retry logic)
        });
    }
  }

  fetchEmails() {
    this.emailService.fetchEmails()
      .subscribe(emails => {
        this.emails = emails;
      }, error => {
        console.error('Error fetching emails:', error);
        // Handle error (show error message or retry logic)
      });
  }
  getId(){
    return this.emailService.getEmailById()
  }

  refuseEmail(emailId: number): void {
    this.emailService.refuseEmail(emailId)
      .subscribe(response => {
        console.log('Email refused successfully:', response);
        // Optionally, update UI or notify user
      }, error => {
        console.error('Error refusing email:', error);
        // Handle error (show error message or retry logic)
      });
  }

  acceptEmail(emailId: number): void {
    this.emailService.acceptEmail(emailId)
      .subscribe(response => {
        console.log('Email accepted successfully:', response);
        // Optionally, update UI or notify user
      }, error => {
        console.error('Error accepting email:', error);
        // Handle error (show error message or retry logic)
      });
  }
}
