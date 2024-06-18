export interface TransferLigne {
    id: number;
    numero_de_ligne: string;
    date_transfer: string;
    ancienne_addresse: string;
    nouvelle_addresse: string;
    statut?: string;
    user_name?: string;
    admin?:string;
  }
  