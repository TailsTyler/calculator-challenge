import { Component } from '@angular/core';

// @Component({
//   selector: 'app-root',
//   templateUrl: './app.component.html',
//   styleUrls: ['./app.component.css']
// })
// export class AppComponent {
//   title = 'calculator';
// }

@Component({
  selector: 'app-root',
  template: `<div class="content"><span>{{ title }} app is running!</span></div>`,
  styles: [`.content { padding: 10px; }`]
})
export class AppComponent {
  title = 'calculator';
}
