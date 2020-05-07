import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  Person: File;

  constructor(private http: HttpClient) {}


  onfileChanged(event: any) {
    this.Person = event.target.files[0];
  }

  newdata() {
    const uploadData = new FormData();
    uploadData.append('Person', this.Person, this.Person.name);
    this.http.post('http://127.0.0.1:8000/person/', uploadData).subscribe(
      data => console.log(data),
      error => console.log(error)
    );
  }
}