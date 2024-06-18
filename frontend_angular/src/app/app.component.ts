import { Component, OnInit } from '@angular/core';


@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent{
  title = 'angular-frontend';
  data: any;

  constructor() {}

  // ngOnInit() {
  //   this.apiService.getData().subscribe(
  //     (response: any) => {
  //       console.log('Response from API:', response);
  //       this.data = response;
  //     },
  //     (error: any) => {
  //       console.error('Error fetching data:', error);
  //     }
  //   );
  // }
}
