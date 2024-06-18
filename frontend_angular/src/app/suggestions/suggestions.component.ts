import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../auth.service';
import { myDataService  } from '../mydata.service'; // Adjust the path as needed
import { Suggestion } from './suggestions.model';

@Component({
  selector: 'app-suggestions',
  templateUrl: './suggestions.component.html',
  styleUrls: ['./suggestions.component.css']
})
export class SUGGESTIONSComponent implements OnInit {
  suggestions: Suggestion[] = [];
  role: string | null;
  suggestionForm: FormGroup;

  constructor(
    private myDataService: myDataService ,
    private fb: FormBuilder,
    private authService: AuthService
  ) {
    this.role = '';
    this.suggestionForm = this.fb.group({
      sujet: ['', Validators.required],
      description: ['', Validators.required],
    });
  }

  ngOnInit(): void {
    this.role = this.authService.getRole();
    if (this.role === 'admin') {
      this.loadSuggestions();
    }
  }

  loadSuggestions() {
    this.myDataService.getSuggestions().subscribe(
      data => {
        this.suggestions = data;
      },
      error => {
        console.error('Error loading suggestions: ', error);
      }
    );
  }

  addSuggestion() {
    if (this.suggestionForm.valid) {
      this.myDataService.addSuggestion(this.suggestionForm.value).subscribe(
        () => {
          this.loadSuggestions();
          this.suggestionForm.reset();
        },
        error => {
          console.error('Error adding suggestion: ', error);
        }
      );
    }
  }

  acceptSuggestion(suggestion: Suggestion) {
    this.myDataService.acceptSuggestion(suggestion).subscribe(
      () => {
        this.loadSuggestions();
      },
      error => {
        console.error('Error accepting suggestion: ', error);
      }
    );
  }

  rejectSuggestion(suggestion: Suggestion) {
    this.myDataService.rejectSuggestion(suggestion).subscribe(
      () => {
        this.loadSuggestions();
      },
      error => {
        console.error('Error rejecting suggestion: ', error);
      }
    );
   }
}
