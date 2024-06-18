export interface MigrationOffre {
    id?: number; // Optional since it will be assigned by Django
    client_name?: string;
    numerooffre: number;
    dateemission?: string; // Optional since it will be assigned by Django
    ancienne_offre: string;
    nouvelle_offre: string;
    statut?: string; // Optional since it will be assigned by Django
    admin?: string; // Optional since it will be assigned by Django
  }
  