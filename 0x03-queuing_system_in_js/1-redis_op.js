import { createClient }  from 'redis';

const client = createClient();

const connectToRedis = async () => {
  client.on('connect', () => {
    console.log('Redis client connected to the server', () => {
      displaySchoolValue('Holberton');
      setNewSchool('HolbertonSanFrancisco', '100');
      displaySchoolValue('HolbertonSanFrancisco');
    });
  });
  client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  });

};

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, client.print);
};

const displaySchoolValue = (schoolName) => {
  const val = client.get(schoolName);
  console.log(val);
};

connectToRedis();