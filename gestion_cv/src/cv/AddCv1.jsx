import React, { Component } from 'react';
import './AddCv1.css'
import axios from 'axios';



class AddCv1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      name: '',
      email: '',
      fullName: '',
      tel: '',
      job: '',
      entreprise: '',
      startDate: '',
      endDate: '',
      description: '',
      diploma: '',
      establishment: '',
      dateObtained: ''
    };
  }

  handleNameChange = (event) => {
    this.setState({ name: event.target.value });
  };

  handleEmailChange = (event) => {
    this.setState({ email: event.target.value });
  };

  handleFullNameChange = (event) => {
    this.setState({ fullName: event.target.value });
  };

  handleTelChange = (event) => {
    this.setState({ tel: event.target.value });
  };

  handleJobChange = (event) => {
    this.setState({ job: event.target.value });
  };

  handleEntrepriseChange = (event) => {
    this.setState({ entreprise: event.target.value });
  };

  handleStartDateChange = (event) => {
    this.setState({ startDate: event.target.value });
  };

  handleEndDateChange = (event) => {
    this.setState({ endDate: event.target.value });
  };

  handleDescriptionChange = (event) => {
    this.setState({ description: event.target.value });
  };

  handleDiplomaChange = (event) => {
    this.setState({ diploma: event.target.value });
  };

  handleEstablishmentChange = (event) => {
    this.setState({ establishment: event.target.value });
  };

  handleDateObtainedChange = (event) => {
    this.setState({ dateObtained: event.target.value });
  };

  handleSubmit = async (event) => {
    event.preventDefault();
    const data = {
      name: this.state.name,
      email: this.state.email,
      fullName: this.state.fullName,
      tel: this.state.tel,
      job: this.state.job,
      entreprise: this.state.entreprise,
      startDate: this.state.startDate,
      endDate: this.state.endDate,
      description: this.state.description,
      diploma: this.state.diploma,
      establishment: this.state.establishment,
      dateObtained: this.state.dateObtained
    };
    console.log(data);
    
    axios.get('/')
    .then(response => {
      console.log(response.data);
    })
    .catch(error => {
      console.log(error);
    });
  };

  render() {
    return (
      <div className='content-form'>
        <h1>Remplissez les informations pour ajouter votre CV</h1>
        <form onSubmit={this.handleSubmit}>
          <div className='personal-info'>
            <h2>Informations personnelles</h2>
            <label>Nom</label>
            <input type='text' value={this.state.name} onChange={this.handleNameChange} />

            <label>Prénom</label>
            <input type='text' value={this.state.fullName} onChange={this.handleFullNameChange} />

            <label>Email</label>
            <input type='email' value={this.state.email} onChange={this.handleEmailChange} />

            <label>Téléphone</label>
            <input type='tel' value={this.state.tel} onChange={this.handleTelChange} />
          </div>

          <div className='professional-experience'>
            <h2>Expériences professionnelles</h2>
            <label>Poste</label>
            <input type='text' value={this.state.job} onChange={this.handleJobChange} />

            <label>Entreprise</label>
            <input type='text' value={this.state.entreprise} onChange={this.handleEntrepriseChange} />

            <label>Date de début</label>
            <input type='date' value={this.state.startDate} onChange={this.handleStartDateChange} />

            <label>Date de fin</label>
            <input type='date' value={this.state.endDate} onChange={this.handleEndDateChange} />

            <label>Description</label>
            <textarea value={this.state.description} onChange={this.handleDescriptionChange}></textarea>
          </div>

          <div className='education'>
            <h2>Formations</h2>
            <label>Diplôme</label>
            <input type='text' value={this.state.diploma} onChange={this.handleDiplomaChange} />

            <label>Etablissement</label>
            <input type='text' value={this.state.establishment} onChange={this.handleEstablishmentChange} />

            <label>Date d'obtention</label>
            <input type='date' value={this.state.dateObtained} onChange={this.handleDateObtainedChange} />
          </div>

          <button type='submit' className='primary'>Submit</button>
        </form>
      </div>

    );
  }
}



export default AddCv1;

const instance = axios.create({
  baseURL: '/api', // c'est la partie de l'URL qui sera redirigée vers votre backend via le proxy
  timeout: 10000, // temps d'attente maximum pour une requête
});