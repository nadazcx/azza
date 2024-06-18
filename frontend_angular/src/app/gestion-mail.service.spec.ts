import { TestBed } from '@angular/core/testing';

import { GestionMailService } from './gestion-mail.service';

describe('GestionMailService', () => {
  let service: GestionMailService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(GestionMailService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
