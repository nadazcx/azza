import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { myDataService  } from '../mydata.service'; // Adjust the path as needed
import { MigrationOffre } from './migration-d-offre.model';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-migration-d-offre',
  templateUrl: './migration-d-offre.component.html',
  styleUrls: ['./migration-d-offre.component.css']
})
export class MIGRATIONDOFFREComponent implements OnInit {
  MigrationForm!: FormGroup;
  role: string = ''; // Assuming you'll set this from authService
  migrationOffres: MigrationOffre[] = [];

  constructor(
    private formBuilder: FormBuilder,
    private dataService: myDataService,
    private authService: AuthService
  ) {
    this.role = '';
   }

  ngOnInit(): void {
    this.MigrationForm = this.formBuilder.group({
      numero: ['', Validators.required],
      ancienneOffre: ['', Validators.required],
      nouvelleOffre: ['', Validators.required],
    });

    this.role = this.authService.getRole() ?? '';
    if (this.role === 'admin') {
      this.loadMigrationOffres();
    } else {
      this.loadMigrationOffres(); // Load migration offres initially
    }
  }

  onSubmit(): void {
    if (this.MigrationForm.valid) {
      const formData = this.MigrationForm.value;
      const migrationOffre: MigrationOffre = {
        numerooffre: formData.numero,
        ancienne_offre: formData.ancienneOffre,
        nouvelle_offre: formData.nouvelleOffre
      };

      this.dataService.createMigrationOffre(migrationOffre).subscribe(
        response => {
          console.log('Migration Offre added successfully!', response);
          this.MigrationForm.reset();
          this.loadMigrationOffres();
        },
        error => {
          console.error('Error adding Migration Offre:', error);
        }
      );
    } else {
      this.MigrationForm.markAllAsTouched();
    }
  }

  accepterOffre(migrationOffres: MigrationOffre): void {
    const offreId = migrationOffres.id ?? 0; // Use a default value if id is undefined

    this.dataService.accepterMigrationOffre(offreId).subscribe(
      response => {
        console.log('Offre accepted successfully!', response);
        this.loadMigrationOffres();
      },
      error => {
        console.error('Error accepting Offre:', error);
      }
    );
  }

  refuserOffre(migrationOffres: MigrationOffre): void {
    const offreId = migrationOffres.id ?? 0; // Use a default value if id is undefined
    this.dataService.refuserMigrationOffre(offreId).subscribe(
      response => {
        console.log('Offre refused successfully!', response);
        this.loadMigrationOffres();
      },
      error => {
        console.error('Error refusing Offre:', error);
      }
    );
  }

  private loadMigrationOffres(): void {
    this.dataService.getMigrationOffres().subscribe(
      migrationOffres => {
        this.migrationOffres = migrationOffres;
      },
      error => {
        console.error('Error loading Migration Offres:', error);
      }
    );
  }
}
